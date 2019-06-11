using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UpdateLadderText : MonoBehaviour {
    
    public enum Side {
        x, y, z
    }

    public Text text;
    public Side side;

    private float height_ratio;
    private float distance_ratio;

    // Start is called before the first frame update
    void Start() {
        height_ratio = 1.5051F;
        distance_ratio = -9.505F;
    }

    // Update is called once per frame
    void Update() {
        switch (side) {
            case (Side.x):
                break;
            case (Side.y):
                float height = transform.position.y/height_ratio;
                text.text = string.Format("{0:0.00}m", height);
                break;
            case (Side.z):
                float distance = (transform.position.y);
                text.text = string.Format("{0:0.00}m", distance);
                break;
        }
    }
}