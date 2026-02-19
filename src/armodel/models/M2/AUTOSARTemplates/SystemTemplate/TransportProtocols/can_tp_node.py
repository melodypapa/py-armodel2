"""CanTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 611)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)


class CanTpNode(Identifiable):
    """AUTOSAR CanTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connector: Optional[Any]
    max_fc_wait: Optional[Integer]
    st_min: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    tp_address: Optional[CanTpAddress]
    def __init__(self) -> None:
        """Initialize CanTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.max_fc_wait: Optional[Integer] = None
        self.st_min: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.tp_address: Optional[CanTpAddress] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpNode":
        """Deserialize XML element to CanTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpNode object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connector
        child = ARObject._find_child_element(element, "CONNECTOR")
        if child is not None:
            connector_value = child.text
            obj.connector = connector_value

        # Parse max_fc_wait
        child = ARObject._find_child_element(element, "MAX-FC-WAIT")
        if child is not None:
            max_fc_wait_value = child.text
            obj.max_fc_wait = max_fc_wait_value

        # Parse st_min
        child = ARObject._find_child_element(element, "ST-MIN")
        if child is not None:
            st_min_value = child.text
            obj.st_min = st_min_value

        # Parse timeout_ar
        child = ARObject._find_child_element(element, "TIMEOUT-AR")
        if child is not None:
            timeout_ar_value = child.text
            obj.timeout_ar = timeout_ar_value

        # Parse timeout_as
        child = ARObject._find_child_element(element, "TIMEOUT-AS")
        if child is not None:
            timeout_as_value = child.text
            obj.timeout_as = timeout_as_value

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "CanTpAddress")
            obj.tp_address = tp_address_value

        return obj



class CanTpNodeBuilder:
    """Builder for CanTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpNode = CanTpNode()

    def build(self) -> CanTpNode:
        """Build and return CanTpNode object.

        Returns:
            CanTpNode instance
        """
        # TODO: Add validation
        return self._obj
