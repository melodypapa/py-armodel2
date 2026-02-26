"""BinaryManifest module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.cp_software_cluster_binary_manifest_descriptor import (
        CpSoftwareClusterBinaryManifestDescriptor,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_provide_resource import (
        BinaryManifestProvideResource,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
        BinaryManifestResource,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_require_resource import (
        BinaryManifestRequireResource,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource_definition import (
        BinaryManifestResourceDefinition,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
        BinaryManifestItem,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_definition import (
        BinaryManifestItemDefinition,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
        BinaryManifestAddressableObject,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
        BinaryManifestItemValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_numerical_value import (
        BinaryManifestItemNumericalValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_pointer_value import (
        BinaryManifestItemPointerValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_meta_data_field import (
        BinaryManifestMetaDataField,
    )

__all__ = [
    "BinaryManifestAddressableObject",
    "BinaryManifestItem",
    "BinaryManifestItemDefinition",
    "BinaryManifestItemNumericalValue",
    "BinaryManifestItemPointerValue",
    "BinaryManifestItemValue",
    "BinaryManifestMetaDataField",
    "BinaryManifestProvideResource",
    "BinaryManifestRequireResource",
    "BinaryManifestResource",
    "BinaryManifestResourceDefinition",
    "CpSoftwareClusterBinaryManifestDescriptor",
]
