using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Valve.VR.InteractionSystem {
    public class InteractableNetworked : Interactable
    {
        public Hand hand;
        protected override void OnAttachedToHand(Hand hand) {
            base.OnAttachedToHand(hand);
            this.hand = hand;
        }

        protected override void OnDetachedFromHand(Hand hand) {
            base.OnDetachedFromHand(hand);
            this.hand = null;
        }
    }
}