using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class UpdateOilText : MonoBehaviour
{

    public enum Property {
        radius, area, volume
    }

    public Text text;
    public Property property;
    private double ratio = 2.18509686118; 

    // Start is called before the first frame update
    void Start() {
    }

    // Update is called once per frame
    void Update()
    {
        switch (property) {
            case (Property.radius):
                double radius = transform.localScale.x * ratio;
                text.text = string.Format("Radius = {0:0}m", radius);
                break;
            case (Property.area):
                double area = Math.Pow((transform.localScale.x * ratio), 2) * Math.PI;
                text.text = string.Format("Area = {0:0}m\x00B2", area);
                break;
            case (Property.volume):
                double volume = Math.Pow((transform.localScale.x * ratio), 2) * Math.PI * 0.1;
                text.text = string.Format("Volume = {0:0}m\x00B3", volume);
                break;
        }
    }
}
