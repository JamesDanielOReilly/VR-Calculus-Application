using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Valve.VR.InteractionSystem {
    public class ObtainableObject : Photon.PunBehaviour
    {

        [PunRPC]
        void RPCDetachOthers() {
            Hand hand = GetComponent<InteractableNetworked>().hand;
            hand.DetachObject(gameObject);
        }
        public void TakeOwnership()
        {
            Debug.Log("Taking ownership");
            base.photonView.RequestOwnership();
            this.photonView.RPC("RPCDetachOthers", PhotonTargets.Others);
        }

        private void Update()
        {
            if (!photonView.isMine)
            {
                gameObject.GetComponent<Rigidbody>().useGravity = false;
            }
        }
        
    }
}