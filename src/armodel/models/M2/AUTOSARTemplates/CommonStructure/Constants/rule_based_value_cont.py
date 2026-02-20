"""RuleBasedValueCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedValueCont(ARObject):
    """AUTOSAR RuleBasedValueCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rule_based: Optional[Any]
    sw_arraysize_ref: Optional[ARRef]
    unit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RuleBasedValueCont."""
        super().__init__()
        self.rule_based: Optional[Any] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedValueCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize rule_based
        if self.rule_based is not None:
            serialized = ARObject._serialize_item(self.rule_based, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE-BASED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_arraysize_ref
        if self.sw_arraysize_ref is not None:
            serialized = ARObject._serialize_item(self.sw_arraysize_ref, "ValueList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ARRAYSIZE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = ARObject._serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueCont":
        """Deserialize XML element to RuleBasedValueCont object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedValueCont object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rule_based
        child = ARObject._find_child_element(element, "RULE-BASED")
        if child is not None:
            rule_based_value = child.text
            obj.rule_based = rule_based_value

        # Parse sw_arraysize_ref
        child = ARObject._find_child_element(element, "SW-ARRAYSIZE-REF")
        if child is not None:
            sw_arraysize_ref_value = ARRef.deserialize(child)
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse unit_ref
        child = ARObject._find_child_element(element, "UNIT-REF")
        if child is not None:
            unit_ref_value = ARRef.deserialize(child)
            obj.unit_ref = unit_ref_value

        return obj



class RuleBasedValueContBuilder:
    """Builder for RuleBasedValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueCont = RuleBasedValueCont()

    def build(self) -> RuleBasedValueCont:
        """Build and return RuleBasedValueCont object.

        Returns:
            RuleBasedValueCont instance
        """
        # TODO: Add validation
        return self._obj
