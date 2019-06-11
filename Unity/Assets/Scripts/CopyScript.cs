using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CopyScript : Photon.MonoBehaviour
{

    public int index = 1;
    // Start is called before the first frame update
    void Start() {
        if (photonView.isMine)
        {
            GetComponent<PhotonVoiceRecorder>().enabled = true;
        }
    }

    // Update is called once per frame
    void Update() {
        if(photonView.isMine) {
            switch (index) {
                case (1): 
                    transform.position = OculusManager.Instance.head.transform.position;
                    transform.rotation = OculusManager.Instance.head.transform.rotation;
                break;
                case (2):
                    transform.position = OculusManager.Instance.leftHand.transform.position;
                    transform.rotation = OculusManager.Instance.leftHand.transform.rotation;
                break;
                case (3):
                    transform.position = OculusManager.Instance.rightHand.transform.position;
                    transform.rotation = OculusManager.Instance.rightHand.transform.rotation;
                break;
            }
        }
    }
}