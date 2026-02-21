"""ConstantSpecificationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantSpecificationMapping(ARObject):
    """AUTOSAR ConstantSpecificationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_constant_ref: Optional[ARRef]
    impl_constant_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ConstantSpecificationMapping."""
        super().__init__()
        self.appl_constant_ref: Optional[ARRef] = None
        self.impl_constant_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ConstantSpecificationMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantSpecificationMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize appl_constant_ref
        if self.appl_constant_ref is not None:
            serialized = SerializationHelper.serialize_item(self.appl_constant_ref, "ConstantSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPL-CONSTANT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize impl_constant_ref
        if self.impl_constant_ref is not None:
            serialized = SerializationHelper.serialize_item(self.impl_constant_ref, "ConstantSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPL-CONSTANT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMapping":
        """Deserialize XML element to ConstantSpecificationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecificationMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantSpecificationMapping, cls).deserialize(element)

        # Parse appl_constant_ref
        child = SerializationHelper.find_child_element(element, "APPL-CONSTANT-REF")
        if child is not None:
            appl_constant_ref_value = ARRef.deserialize(child)
            obj.appl_constant_ref = appl_constant_ref_value

        # Parse impl_constant_ref
        child = SerializationHelper.find_child_element(element, "IMPL-CONSTANT-REF")
        if child is not None:
            impl_constant_ref_value = ARRef.deserialize(child)
            obj.impl_constant_ref = impl_constant_ref_value

        return obj



class ConstantSpecificationMappingBuilder:
    """Builder for ConstantSpecificationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecificationMapping = ConstantSpecificationMapping()

    def build(self) -> ConstantSpecificationMapping:
        """Build and return ConstantSpecificationMapping object.

        Returns:
            ConstantSpecificationMapping instance
        """
        # TODO: Add validation
        return self._obj
