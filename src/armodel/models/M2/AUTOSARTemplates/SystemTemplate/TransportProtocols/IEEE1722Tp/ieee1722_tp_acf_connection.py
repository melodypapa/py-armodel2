"""IEEE1722TpAcfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 656)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """AUTOSAR IEEE1722TpAcfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acf_transporteds: list[IEEE1722TpAcfBus]
    collection: Optional[TimeValue]
    mixed_bus_type: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfConnection."""
        super().__init__()
        self.acf_transporteds: list[IEEE1722TpAcfBus] = []
        self.collection: Optional[TimeValue] = None
        self.mixed_bus_type: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfConnection":
        """Deserialize XML element to IEEE1722TpAcfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse acf_transporteds (list)
        obj.acf_transporteds = []
        for child in ARObject._find_all_child_elements(element, "ACF-TRANSPORTEDS"):
            acf_transporteds_value = ARObject._deserialize_by_tag(child, "IEEE1722TpAcfBus")
            obj.acf_transporteds.append(acf_transporteds_value)

        # Parse collection
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_value = child.text
            obj.collection = collection_value

        # Parse mixed_bus_type
        child = ARObject._find_child_element(element, "MIXED-BUS-TYPE")
        if child is not None:
            mixed_bus_type_value = child.text
            obj.mixed_bus_type = mixed_bus_type_value

        return obj



class IEEE1722TpAcfConnectionBuilder:
    """Builder for IEEE1722TpAcfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfConnection = IEEE1722TpAcfConnection()

    def build(self) -> IEEE1722TpAcfConnection:
        """Build and return IEEE1722TpAcfConnection object.

        Returns:
            IEEE1722TpAcfConnection instance
        """
        # TODO: Add validation
        return self._obj
