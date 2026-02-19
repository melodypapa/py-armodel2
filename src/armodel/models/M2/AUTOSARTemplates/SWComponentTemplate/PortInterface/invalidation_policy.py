"""InvalidationPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InvalidationPolicy(ARObject):
    """AUTOSAR InvalidationPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_ref: Optional[ARRef]
    handle_invalid_enum: Optional[HandleInvalidEnum]
    def __init__(self) -> None:
        """Initialize InvalidationPolicy."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize InvalidationPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_invalid_enum
        if self.handle_invalid_enum is not None:
            serialized = ARObject._serialize_item(self.handle_invalid_enum, "HandleInvalidEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-INVALID-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InvalidationPolicy":
        """Deserialize XML element to InvalidationPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InvalidationPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse handle_invalid_enum
        child = ARObject._find_child_element(element, "HANDLE-INVALID-ENUM")
        if child is not None:
            handle_invalid_enum_value = HandleInvalidEnum.deserialize(child)
            obj.handle_invalid_enum = handle_invalid_enum_value

        return obj



class InvalidationPolicyBuilder:
    """Builder for InvalidationPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvalidationPolicy = InvalidationPolicy()

    def build(self) -> InvalidationPolicy:
        """Build and return InvalidationPolicy object.

        Returns:
            InvalidationPolicy instance
        """
        # TODO: Add validation
        return self._obj
