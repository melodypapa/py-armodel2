"""DdsLiveliness AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsLivenessKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLiveliness(ARObject):
    """AUTOSAR DdsLiveliness."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    liveliness_lease: Optional[Float]
    liveness_kind: Optional[DdsLivenessKindEnum]
    def __init__(self) -> None:
        """Initialize DdsLiveliness."""
        super().__init__()
        self.liveliness_lease: Optional[Float] = None
        self.liveness_kind: Optional[DdsLivenessKindEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLiveliness":
        """Deserialize XML element to DdsLiveliness object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsLiveliness object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse liveliness_lease
        child = ARObject._find_child_element(element, "LIVELINESS-LEASE")
        if child is not None:
            liveliness_lease_value = child.text
            obj.liveliness_lease = liveliness_lease_value

        # Parse liveness_kind
        child = ARObject._find_child_element(element, "LIVENESS-KIND")
        if child is not None:
            liveness_kind_value = child.text
            obj.liveness_kind = liveness_kind_value

        return obj



class DdsLivelinessBuilder:
    """Builder for DdsLiveliness."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLiveliness = DdsLiveliness()

    def build(self) -> DdsLiveliness:
        """Build and return DdsLiveliness object.

        Returns:
            DdsLiveliness instance
        """
        # TODO: Add validation
        return self._obj
