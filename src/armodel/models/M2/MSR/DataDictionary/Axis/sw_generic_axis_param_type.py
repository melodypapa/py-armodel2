"""SwGenericAxisParamType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)


class SwGenericAxisParamType(Identifiable):
    """AUTOSAR SwGenericAxisParamType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_constr_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwGenericAxisParamType."""
        super().__init__()
        self.data_constr_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwGenericAxisParamType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwGenericAxisParamType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_constr_ref
        if self.data_constr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_constr_ref, "DataConstr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-CONSTR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParamType":
        """Deserialize XML element to SwGenericAxisParamType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwGenericAxisParamType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwGenericAxisParamType, cls).deserialize(element)

        # Parse data_constr_ref
        child = SerializationHelper.find_child_element(element, "DATA-CONSTR-REF")
        if child is not None:
            data_constr_ref_value = ARRef.deserialize(child)
            obj.data_constr_ref = data_constr_ref_value

        return obj



class SwGenericAxisParamTypeBuilder:
    """Builder for SwGenericAxisParamType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParamType = SwGenericAxisParamType()

    def build(self) -> SwGenericAxisParamType:
        """Build and return SwGenericAxisParamType object.

        Returns:
            SwGenericAxisParamType instance
        """
        # TODO: Add validation
        return self._obj
