using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class RoomSwitcher : MonoBehaviour
{
    private GameObject player;
    public Transform PlayerOneTransform;
    public Transform PlayerTwoTransform;

    public void Start()
    {
        player = GameObject.Find("Player");
    }

    public void GoToApplicationRoom()
    {
        if (PhotonNetwork.player.ID == 1)
        {
            Debug.Log("Transporting player 1 to application room");
            player.transform.position = PlayerOneTransform.position;
        }

        if (PhotonNetwork.player.ID == 2)
        {
            Debug.Log("Transporting player 2 to application room");
            player.transform.position = PlayerTwoTransform.position;
        }
    }
    public void GoToTheoryRoom()
    {
        if (PhotonNetwork.player.ID == 1)
        {
            Debug.Log("Transporting player 1 to theory room");
            player.transform.position = PlayerOneTransform.position;
        }

        if (PhotonNetwork.player.ID == 2)
        {
            Debug.Log("Transporting player 2 to theory room");
            player.transform.position = PlayerTwoTransform.position;
        }
    }

    public void GoToLoadingRoom()
    {
        if (PhotonNetwork.player.ID == 1)
        {
            Debug.Log("Transporting player 1 to loading room");
            player.transform.position = PlayerOneTransform.position;
        }

        if (PhotonNetwork.player.ID == 2)
        {
            Debug.Log("Transporting player 2 to loading room");
            player.transform.position = PlayerTwoTransform.position;
        }
    }
}
