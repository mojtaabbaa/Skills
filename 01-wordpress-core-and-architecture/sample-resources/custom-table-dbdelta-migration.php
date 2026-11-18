<?php
/**
 * Sample Custom Table Migration using WordPress dbDelta()
 */
namespace MyPlugin\Database;

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

class Migration_Manager {

    const DB_VERSION_OPTION = 'myplugin_db_version';
    const CURRENT_DB_VERSION = '1.2.0';

    public static function maybe_upgrade() {
        $installed_ver = get_option( self::DB_VERSION_OPTION, '0.0.0' );

        if ( version_compare( $installed_ver, self::CURRENT_DB_VERSION, '<' ) ) {
            self::run_migrations();
            update_option( self::DB_VERSION_OPTION, self::CURRENT_DB_VERSION );
        }
    }

    private static function run_migrations() {
        global $wpdb;
        $table_name = $wpdb->prefix . 'myplugin_logs';
        $charset_collate = $wpdb->get_charset_collate();

        // Note rules for dbDelta: two spaces after PRIMARY KEY, each field on its own line
        $sql = "CREATE TABLE {$table_name} (
            id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            user_id bigint(20) unsigned NOT NULL DEFAULT 0,
            event_type varchar(64) NOT NULL DEFAULT '',
            payload longtext NOT NULL,
            created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY  (id),
            KEY user_id (user_id),
            KEY event_type (event_type)
        ) {$charset_collate};";

        require_once ABSPATH . 'wp-admin/includes/upgrade.php';
        dbDelta( $sql );
    }
}
