using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObtainableDrive : MonoBehaviour
{
    // Update is called once per frame
    public void transferOwnership()
    {
        // if (transform.parent.gameObject.transform.Find("LadderLinearMapping").gameObject.GetComponent<PhotonView>().ownerId != PhotonNetwork.player.ID)
        // {
        //     transform.parent.gameObject.transform.Find("LadderLinearMapping").gameObject.GetComponent<PhotonView>().TransferOwnership(PhotonNetwork.player.ID);
        // }
    }
}