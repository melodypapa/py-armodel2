"""RtePluginProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 971)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class RtePluginProps(ARObject):
    """AUTOSAR RtePluginProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    associated_ref: Optional[ARRef]
    associated_rte_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RtePluginProps."""
        super().__init__()
        self.associated_ref: Optional[ARRef] = None
        self.associated_rte_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RtePluginProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize associated_ref
        if self.associated_ref is not None:
            serialized = SerializationHelper.serialize_item(self.associated_ref, "EcucContainerValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSOCIATED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize associated_rte_ref
        if self.associated_rte_ref is not None:
            serialized = SerializationHelper.serialize_item(self.associated_rte_ref, "EcucContainerValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSOCIATED-RTE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtePluginProps":
        """Deserialize XML element to RtePluginProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RtePluginProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse associated_ref
        child = SerializationHelper.find_child_element(element, "ASSOCIATED-REF")
        if child is not None:
            associated_ref_value = ARRef.deserialize(child)
            obj.associated_ref = associated_ref_value

        # Parse associated_rte_ref
        child = SerializationHelper.find_child_element(element, "ASSOCIATED-RTE-REF")
        if child is not None:
            associated_rte_ref_value = ARRef.deserialize(child)
            obj.associated_rte_ref = associated_rte_ref_value

        return obj



class RtePluginPropsBuilder:
    """Builder for RtePluginProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtePluginProps = RtePluginProps()

    def build(self) -> RtePluginProps:
        """Build and return RtePluginProps object.

        Returns:
            RtePluginProps instance
        """
        # TODO: Add validation
        return self._obj
