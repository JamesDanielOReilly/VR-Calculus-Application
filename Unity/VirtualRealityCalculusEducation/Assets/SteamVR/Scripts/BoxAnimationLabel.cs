using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class BoxAnimationLabel : MonoBehaviour {

    public Text Label;

	// Update is called once per frame
	void Update () {
        Vector3 namePos = Camera.main.WorldToScreenPoint(this.transform.position);
        Label.transform.position = namePos;
	}
}
