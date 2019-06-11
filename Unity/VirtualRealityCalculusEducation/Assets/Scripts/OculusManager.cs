using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OculusManager : MonoBehaviour
{

    public GameObject head;
    public GameObject leftHand;
    public GameObject rightHand;
    public static OculusManager Instance;

    void Awake() {
        if (Instance == null)
            Instance = this;
    }

    void onDestroy() {
        if (Instance == this)
            Instance = null;
    }
}
