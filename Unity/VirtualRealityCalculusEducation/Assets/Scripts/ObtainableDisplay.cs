using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObtainableDisplay : Photon.PunBehaviour
{
    private void onGrab() {
        base.photonView.RequestOwnership();
    }

    // Update is called once per frame
    private void Update()
    {
        if(base.photonView.owner == PhotonNetwork.player) {

        }
    }
}
