using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class onDetached : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        gameObject.GetComponent<isHandAttached>().enabled = true;
    }
}
