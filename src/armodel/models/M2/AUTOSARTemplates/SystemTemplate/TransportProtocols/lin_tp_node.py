"""LinTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 614)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpNode(Identifiable):
    """AUTOSAR LinTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connector: Optional[Any]
    drop_not: Optional[Boolean]
    max_number_of: Optional[Integer]
    p2_max: Optional[TimeValue]
    p2_timing: Optional[TimeValue]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize LinTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.drop_not: Optional[Boolean] = None
        self.max_number_of: Optional[Integer] = None
        self.p2_max: Optional[TimeValue] = None
        self.p2_timing: Optional[TimeValue] = None
        self.tp_address: Optional[TpAddress] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpNode":
        """Deserialize XML element to LinTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpNode object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connector
        child = ARObject._find_child_element(element, "CONNECTOR")
        if child is not None:
            connector_value = child.text
            obj.connector = connector_value

        # Parse drop_not
        child = ARObject._find_child_element(element, "DROP-NOT")
        if child is not None:
            drop_not_value = child.text
            obj.drop_not = drop_not_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse p2_max
        child = ARObject._find_child_element(element, "P2-MAX")
        if child is not None:
            p2_max_value = child.text
            obj.p2_max = p2_max_value

        # Parse p2_timing
        child = ARObject._find_child_element(element, "P2-TIMING")
        if child is not None:
            p2_timing_value = child.text
            obj.p2_timing = p2_timing_value

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_address = tp_address_value

        return obj



class LinTpNodeBuilder:
    """Builder for LinTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpNode = LinTpNode()

    def build(self) -> LinTpNode:
        """Build and return LinTpNode object.

        Returns:
            LinTpNode instance
        """
        # TODO: Add validation
        return self._obj
