package fr.vivaneo.guide;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
    }

    public void showRestaurant(View view) {
        Intent intentRestaurant = new Intent(HomeActivity.this, ListingActivity.class);

        // envoyer un parametre
        intentRestaurant.putExtra("isRestaurant", true);

        startActivity(intentRestaurant);
    }

    public void showHotel(View view) {
        Intent intentHotel = new Intent(HomeActivity.this, ListingActivity.class);

        // envoyer un parametre
        intentHotel.putExtra("isRestaurant", false);

        startActivity(intentHotel);
    }
}