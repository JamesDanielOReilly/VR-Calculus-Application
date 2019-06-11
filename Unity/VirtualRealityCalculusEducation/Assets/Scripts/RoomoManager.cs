using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RoomoManager : MonoBehaviour
{
    public GameObject PlayerOneHead;
    public GameObject PlayerTwoHead;
    public GameObject LeftHandPrefab;
    public GameObject RightHandPrefab;

    public Transform PlayerOneTransform;
    public Transform PlayerTwoTransform;

    private GameObject player;

    // This is used to intialise the players
    void Start()
    {
        player = GameObject.Find("Player");

        Debug.Log("Started");

        if (PhotonNetwork.player.ID % 2 == 1) {
            Debug.Log("Spawning player one head");
            player.transform.position = PlayerOneTransform.position;
            player.transform.rotation = PlayerOneTransform.rotation;
            PhotonNetwork.Instantiate(PlayerOneHead.name, OculusManager.Instance.head.transform.position, OculusManager.Instance.head.transform.rotation, 0);
        } else if (PhotonNetwork.player.ID % 2 == 0) {
            Debug.Log("Spawning player one head");
            player.transform.position = PlayerTwoTransform.position;
            player.transform.rotation = PlayerTwoTransform.rotation;
            PhotonNetwork.Instantiate(PlayerTwoHead.name, OculusManager.Instance.head.transform.position, OculusManager.Instance.head.transform.rotation, 0);
        }
        PhotonNetwork.Instantiate(LeftHandPrefab.name, OculusManager.Instance.leftHand.transform.position, OculusManager.Instance.leftHand.transform.rotation, 0);
        PhotonNetwork.Instantiate(RightHandPrefab.name, OculusManager.Instance.rightHand.transform.position, OculusManager.Instance.rightHand.transform.rotation, 0);

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape)) {
           Application.Quit(); 
        }
    }
}
