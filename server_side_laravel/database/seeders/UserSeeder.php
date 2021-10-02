<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        User::create(['name' => 'ksme_admin', 'email' => 'navidproject283@gmail.com', 'password' => bcrypt('ksmeAdmin123@321'), 'is_admin' => 1]);
    }
}
