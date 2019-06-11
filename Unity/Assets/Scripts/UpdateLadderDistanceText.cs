using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class UpdateLadderDistanceText : MonoBehaviour {
    
    public Text text;

    private double height_ratio;
    private float distance_ratio;

    // Start is called before the first frame update
    void Start() {
        height_ratio = 1.504d;
    }

    // Update is called once per frame
    void Update() {
       double height = transform.position.y/height_ratio;
       double double_distance = Math.Sqrt(16 - Math.Pow(height, 2));
       float distance = (float)double_distance;
       text.text = string.Format("{0:0.00}m", distance);
    }
}