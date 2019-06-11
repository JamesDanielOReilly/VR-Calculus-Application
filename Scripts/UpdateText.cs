using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UpdateText : MonoBehaviour {
    
    public enum Side {
        x, y, z
    }

    public Text lengthText;
    public Side side;

    // Start is called before the first frame update
    void Start() {
        
    }

    // Update is called once per frame
    void Update() {
        switch (side) {
            case (Side.x):
                float length = transform.localScale.x * 12;
                lengthText.text = string.Format("{0:0}cm", length);
                break;
            case (Side.y):
                float height = transform.localScale.y * 12;
                lengthText.text = string.Format("{0:0}cm", height);
                break;
            case (Side.z):
                float width = transform.localScale.z * 12;
                lengthText.text = string.Format("{0:0}cm", width);
                break;
        }
    }
}
