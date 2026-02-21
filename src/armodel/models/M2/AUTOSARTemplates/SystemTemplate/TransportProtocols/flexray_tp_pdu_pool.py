"""FlexrayTpPduPool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayTpPduPool(Identifiable):
    """AUTOSAR FlexrayTpPduPool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    n_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FlexrayTpPduPool."""
        super().__init__()
        self.n_pdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpPduPool to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpPduPool, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize n_pdu_refs (list to container "N-PDU-REFS")
        if self.n_pdu_refs:
            wrapper = ET.Element("N-PDU-REFS")
            for item in self.n_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "NPdu")
                if serialized is not None:
                    child_elem = ET.Element("N-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpPduPool":
        """Deserialize XML element to FlexrayTpPduPool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpPduPool object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpPduPool, cls).deserialize(element)

        # Parse n_pdu_refs (list from container "N-PDU-REFS")
        obj.n_pdu_refs = []
        container = SerializationHelper.find_child_element(element, "N-PDU-REFS")
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
                    obj.n_pdu_refs.append(child_value)

        return obj



class FlexrayTpPduPoolBuilder:
    """Builder for FlexrayTpPduPool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpPduPool = FlexrayTpPduPool()

    def build(self) -> FlexrayTpPduPool:
        """Build and return FlexrayTpPduPool object.

        Returns:
            FlexrayTpPduPool instance
        """
        # TODO: Add validation
        return self._obj
