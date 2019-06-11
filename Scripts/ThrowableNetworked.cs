using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Valve.VR.InteractionSystem {
    public class ThrowableNetworked : Throwable {

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