"""Trigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 45)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class Trigger(Identifiable):
    """AUTOSAR Trigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    trigger_period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize Trigger."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.trigger_period: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize Trigger to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Trigger, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_impl_policy_enum
        if self.sw_impl_policy_enum is not None:
            serialized = ARObject._serialize_item(self.sw_impl_policy_enum, "SwImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-IMPL-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_period
        if self.trigger_period is not None:
            serialized = ARObject._serialize_item(self.trigger_period, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Trigger":
        """Deserialize XML element to Trigger object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Trigger object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Trigger, cls).deserialize(element)

        # Parse sw_impl_policy_enum
        child = ARObject._find_child_element(element, "SW-IMPL-POLICY-ENUM")
        if child is not None:
            sw_impl_policy_enum_value = SwImplPolicyEnum.deserialize(child)
            obj.sw_impl_policy_enum = sw_impl_policy_enum_value

        # Parse trigger_period
        child = ARObject._find_child_element(element, "TRIGGER-PERIOD")
        if child is not None:
            trigger_period_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.trigger_period = trigger_period_value

        return obj



class TriggerBuilder:
    """Builder for Trigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Trigger = Trigger()

    def build(self) -> Trigger:
        """Build and return Trigger object.

        Returns:
            Trigger instance
        """
        # TODO: Add validation
        return self._obj
