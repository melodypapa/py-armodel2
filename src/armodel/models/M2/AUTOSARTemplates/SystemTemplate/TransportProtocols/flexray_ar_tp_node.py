"""FlexrayArTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 602)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpNode(Identifiable):
    """AUTOSAR FlexrayArTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connector_refs: list[Any]
    tp_address_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize FlexrayArTpNode."""
        super().__init__()
        self.connector_refs: list[Any] = []
        self.tp_address_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connector_refs (list to container "CONNECTOR-REFS")
        if self.connector_refs:
            wrapper = ET.Element("CONNECTOR-REFS")
            for item in self.connector_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONNECTOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_address_ref
        if self.tp_address_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_address_ref, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpNode":
        """Deserialize XML element to FlexrayArTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayArTpNode, cls).deserialize(element)

        # Parse connector_refs (list from container "CONNECTOR-REFS")
        obj.connector_refs = []
        container = SerializationHelper.find_child_element(element, "CONNECTOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connector_refs.append(child_value)

        # Parse tp_address_ref
        child = SerializationHelper.find_child_element(element, "TP-ADDRESS-REF")
        if child is not None:
            tp_address_ref_value = ARRef.deserialize(child)
            obj.tp_address_ref = tp_address_ref_value

        return obj



class FlexrayArTpNodeBuilder:
    """Builder for FlexrayArTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpNode = FlexrayArTpNode()

    def build(self) -> FlexrayArTpNode:
        """Build and return FlexrayArTpNode object.

        Returns:
            FlexrayArTpNode instance
        """
        # TODO: Add validation
        return self._obj
