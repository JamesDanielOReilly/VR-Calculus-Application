using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NewBehaviourScript : MonoBehaviour
{
    public void GoToApplicationScene()
    {
        PhotonNetwork.LoadLevel("Applications");
    }

    public void GoToTheoryScene()
    {
        PhotonNetwork.LoadLevel("Theory");
    }
}
