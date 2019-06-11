using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Valve.VR.InteractionSystem;
using Photon;

public class FloatScript : Photon.MonoBehaviour, IPunObservable
{
    public float driverFloat;
    public float currentFloat;
    public bool isHandAttached = false;
    private float photonFloat;
 
    public void onAttached() {
        isHandAttached = true;
        this.photonView.RPC("RPCDetachOthers", PhotonTargets.Others);
    }

    public void onDetached() {
        isHandAttached = false;
    }

    private float Interp(float current, float target, float divisor) {
        if (target != current) {
            return current + (target - current)/divisor;
        } else {
            return target;
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (isHandAttached) {
            driverFloat  = gameObject.GetComponent<LinearDrive>().linearMapping.value;
            currentFloat = gameObject.GetComponent<LinearDrive>().linearMapping.value;
        } else {
            currentFloat = Interp(currentFloat, driverFloat, 10f);
            gameObject.GetComponent<LinearDrive>().linearMapping.value = currentFloat;
        }
    }

    [PunRPC]
    void RPCDetachOthers() {
        onDetached();
    }

    void IPunObservable.OnPhotonSerializeView(PhotonStream stream, PhotonMessageInfo info) {
        Debug.Log("SerializeView running");
        if (stream.isWriting) {            // Send data
            stream.SendNext(driverFloat);
        } else if (stream.isReading) {     // Recieve data
            driverFloat = (float) stream.ReceiveNext();
        }
    }
}
