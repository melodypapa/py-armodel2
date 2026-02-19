"""BinaryManifestItemValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class BinaryManifestItemValue(ARObject, ABC):
    """AUTOSAR BinaryManifestItemValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize BinaryManifestItemValue."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemValue":
        """Deserialize XML element to BinaryManifestItemValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class BinaryManifestItemValueBuilder:
    """Builder for BinaryManifestItemValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemValue = BinaryManifestItemValue()

    def build(self) -> BinaryManifestItemValue:
        """Build and return BinaryManifestItemValue object.

        Returns:
            BinaryManifestItemValue instance
        """
        # TODO: Add validation
        return self._obj
