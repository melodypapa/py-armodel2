"""IPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 341)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 226)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from abc import ABC, abstractmethod


class IPdu(Pdu, ABC):
    """AUTOSAR IPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    contained_i_pdu_props: Optional[ContainedIPduProps]
    def __init__(self) -> None:
        """Initialize IPdu."""
        super().__init__()
        self.contained_i_pdu_props: Optional[ContainedIPduProps] = None

    def serialize(self) -> ET.Element:
        """Serialize IPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize contained_i_pdu_props
        if self.contained_i_pdu_props is not None:
            serialized = SerializationHelper.serialize_item(self.contained_i_pdu_props, "ContainedIPduProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINED-I-PDU-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPdu":
        """Deserialize XML element to IPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPdu, cls).deserialize(element)

        # Parse contained_i_pdu_props
        child = SerializationHelper.find_child_element(element, "CONTAINED-I-PDU-PROPS")
        if child is not None:
            contained_i_pdu_props_value = SerializationHelper.deserialize_by_tag(child, "ContainedIPduProps")
            obj.contained_i_pdu_props = contained_i_pdu_props_value

        return obj



class IPduBuilder:
    """Builder for IPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPdu = IPdu()

    def build(self) -> IPdu:
        """Build and return IPdu object.

        Returns:
            IPdu instance
        """
        # TODO: Add validation
        return self._obj
