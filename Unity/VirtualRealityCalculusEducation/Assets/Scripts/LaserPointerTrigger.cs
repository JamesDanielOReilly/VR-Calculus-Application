using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Valve.VR;
using Valve.VR.InteractionSystem;
using Valve.VR.Extras;

public class LaserPointerTrigger : MonoBehaviour
{
    public SteamVR_Behaviour_Pose pose;
    //public SteamVR_Input_Action pointerButton;
    public SteamVR_LaserPointer laserPointer;
    public SteamVR_Action_Boolean pointerChange;
    public bool pointerOn = false;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        // bool state = laserPointer.GetStateDown(SteamVR_Input_Sources.LeftHand);
        // if (state) {
        //     if (pointerOn == false) {
        //         laserPointer.enabled = true;
        //     }
        //     else {
        //         laserPointer.enabled = false;
        //     }
        // }
    }
}
