using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class TheoryValues : MonoBehaviour
{

    public enum Property {
        x, fx, fstDerivative, sndDerivative
    }

    public Text text;
    public Property property;
    private float xvalue;

    // Start is called before the first frame update
    void Start() {
    }

    // Update is called once per frame
    void Update()
    {
        xvalue = transform.localPosition.z;
        switch (property) {
            case (Property.x):
                text.text = string.Format("x = {0:0.#}", xvalue);
                break;
            case (Property.fx):
                double fx = -4*Math.Pow(xvalue, 3) + 3*Math.Pow(xvalue, 3) + 25*xvalue +6;
                text.text = string.Format("f(x) = {0:0.#}", fx);
                break;
            case (Property.fstDerivative):
                double fstDerivative = -12*Math.Pow(xvalue, 2) + 6*xvalue + 25;
                text.text = string.Format("f'(x) = {0:0.#}", fstDerivative);
                break;
            case (Property.sndDerivative):
            double sndDerivative = -24*xvalue + 6;
            text.text = string.Format("f''(x) = {0:0.#}", sndDerivative);
            break;
        }
    }
}
