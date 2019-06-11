using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HideControllers : Photon.MonoBehaviour
{
    // Update is called once per frame
    void Update()
    {
        if (photonView.isMine) {
            gameObject.GetComponent<MeshRenderer>().enabled = false;

            // Transform temp = this.transform.GetChild(0);
            // temp.transform.GetChild(0).gameObject.GetComponentInChildren<MeshRenderer>().enabled = false;

            
            
            var renderers = this.gameObject.GetComponentsInChildren<Renderer>();
            foreach (var renderer in renderers) {
                renderer.enabled = false;
            } 
        }
    }
}
