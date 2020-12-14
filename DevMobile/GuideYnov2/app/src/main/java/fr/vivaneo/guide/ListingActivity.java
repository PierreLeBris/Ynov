package fr.vivaneo.guide;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

import fr.vivaneo.guide.models.Restaurant;

public class ListingActivity extends AppCompatActivity {

    // déclarations
    private TextView textViewTitle;
    private ListView listViewData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listing);

        // récupération des vues
        textViewTitle = findViewById(R.id.textViewTitle);
        listViewData = findViewById(R.id.listViewData);

        if(getIntent().getExtras() != null) {
            boolean isRestaurant = getIntent().getExtras().getBoolean("isRestaurant");

            if(isRestaurant) {
                textViewTitle.setText("Les Restaurants");

                List<Restaurant> restaurantList = new ArrayList<>();

                restaurantList.add(new Restaurant(
                        "Mac Do",
                        "Fast Food",
                        "info@macdo.fr",
                        "0102030405",
                        "http://www.macdo.fr",
                        "https://intrld.com/wp-content/uploads/2020/03/mcdo-br%C3%A9sil.jpg"
                    )
                );
                restaurantList.add(new Restaurant(
                        "Mac Do 2",
                        "Fast Food",
                        "info@macdo.fr",
                        "0102030405",
                        "http://www.macdo.fr",
                        "https://images.sudouest.fr/2018/02/26/5a940e6b66a4bde56f80a0e1/golden/1200x750/le-wrap-a-ete-retire.jpg"
                    )
                );
                restaurantList.add(new Restaurant(
                        "Mac Do 3",
                        "Fast Food",
                        "info@macdo.fr",
                        "0102030405",
                        "http://www.macdo.fr",
                        "https://images.lanouvellerepublique.fr/image/upload/t_1020w/f_auto/58c2d71b459a453f238b497d.jpg"
                    )
                );

                listViewData.setAdapter(
                        new ArrayAdapter<Restaurant>(
                                ListingActivity.this,
                                R.layout.item_restaurant,
                                restaurantList
                        )
                );


            } else {
                textViewTitle.setText("Les Hôtels");

            }
        }

    }
}