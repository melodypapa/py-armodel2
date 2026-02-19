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
    def serialize(self) -> ET.Element:
        """Serialize LinTpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinTpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connector
        if self.connector is not None:
            serialized = ARObject._serialize_item(self.connector, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize drop_not
        if self.drop_not is not None:
            serialized = ARObject._serialize_item(self.drop_not, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DROP-NOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_max
        if self.p2_max is not None:
            serialized = ARObject._serialize_item(self.p2_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_timing
        if self.p2_timing is not None:
            serialized = ARObject._serialize_item(self.p2_timing, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_address
        if self.tp_address is not None:
            serialized = ARObject._serialize_item(self.tp_address, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpNode":
        """Deserialize XML element to LinTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpNode, cls).deserialize(element)

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
