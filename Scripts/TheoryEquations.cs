using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class TheoryEquations : MonoBehaviour
{

    public enum Equation {
        fx, fstDerivative, sndDerivative
    }

    public Text text;
    public Equation equation;
    string fxString = "f(x) = -4x\x00B3 + 3x\x00B2 + 25x +6";
    string fstDerivativeString = "f '(x) = -12x\x00B2 + 6x + 25";
    string sndDerivativeString = "f ''(x) = -24x + 6";

    // Start is called before the first frame update
    void Start() {
    }

    // Update is called once per frame
    void Update()
    {
        switch (equation) {
            case (Equation.fx):
                text.text = fxString;
                break;
            case (Equation.fstDerivative):
                text.text = fstDerivativeString;
                break;
            case (Equation.sndDerivative):
                text.text = sndDerivativeString;
                break;
        }
    }
}
