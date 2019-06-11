using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class NetManager : MonoBehaviour
{

    public GameObject roomManager;

    //public GameObject headPrefab;
    //public GameObject rightHandPrefab;
    //public GameObject leftHandPrefab;

    //public GameObject CreatedAvatar;
    //public GameObject CreatedRightHand;
    //public GameObject CreatedLeftHand;
    public virtual void Start()
    {
        PhotonNetwork.automaticallySyncScene = true;
        PhotonNetwork.ConnectUsingSettings("1 ." + SceneManagerHelper.ActiveSceneBuildIndex);
        PhotonNetwork.autoJoinLobby = true;
        var temp = PhotonVoiceNetwork.Client;
    }


    // below, we implement some callbacks of PUN
    // you can find PUN's callbacks in the class PunBehaviour or in enum PhotonNetworkingMessage


    public virtual void OnConnectedToMaster()
    {
    }

    public virtual void OnJoinedLobby()
    {
        Debug.Log("OnJoinedLobby(). This client is connected and does get a room-list, which gets stored as PhotonNetwork.GetRoomList(). This script now calls: PhotonNetwork.JoinRandomRoom();");
        PhotonNetwork.JoinOrCreateRoom("hobbs", new RoomOptions() { MaxPlayers = 8}, null);
    }

    /* public virtual void OnPhotonRandomJoinFailed()
    {
        Debug.Log("OnPhotonRandomJoinFailed() was called by PUN. No random room available, so we create one. Calling: PhotonNetwork.CreateRoom(null, new RoomOptions() {maxPlayers = 4}, null);");
        PhotonNetwork.CreateRoom(null, new RoomOptions() { MaxPlayers = 4 }, null);
    }*/

    // the following methods are implemented to give you some context. re-implement them as needed.

    public virtual void OnFailedToConnectToPhoton(DisconnectCause cause)
    {
        Debug.LogError("Cause: " + cause);
    }

    public void OnJoinedRoom()
    {
        Debug.Log("OnJoinedRoom() called by PUN. Now this client is in a room. From here on, your game would be running. For reference, all callbacks are listed in enum: PhotonNetworkingMessage");
        roomManager.SetActive(true);
        //CreatedAvatar = PhotonNetwork.Instantiate(headPrefab.name, OculusManager.Instance.head.transform.position, OculusManager.Instance.head.transform.rotation, 0);
        //CreatedLeftHand = PhotonNetwork.Instantiate(leftHandPrefab.name, OculusManager.Instance.leftHand.transform.position, OculusManager.Instance.leftHand.transform.rotation, 0);
        //CreatedRightHand = PhotonNetwork.Instantiate(rightHandPrefab.name, OculusManager.Instance.rightHand.transform.position, OculusManager.Instance.rightHand.transform.rotation, 0);
        // leftHand.transform.GetChild(0).GetChild(0).gameObject.GetComponent<MeshRenderer>().enabled = false;
        // rightHand.transform.GetChild(0).GetChild(0).gameObject.GetComponent<MeshRenderer>().enabled = false;
        // avatar.transform.GetChild(0).GetChild(0).gameObject.GetComponent<MeshRenderer>().enabled = false;
    }

    // public override void OnOwnershipRequest(Object[] viewAndPlayer) {
    //     PhotonView view = viewAndPlayer[0] as PhotonView;
    //     PhotonPlayer requestingPlayer = viewAndPlayer[1] as PhotonPlayer;

    //     base.photonView.TransferOwnership(requestingPlayer);
    // }
}
