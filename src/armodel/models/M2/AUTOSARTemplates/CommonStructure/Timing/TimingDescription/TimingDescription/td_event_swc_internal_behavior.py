"""TDEventSwcInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class TDEventSwcInternalBehavior(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    runnable_ref: Optional[ARRef]
    td_event_swc_behavior_type: Optional[Any]
    variable_access_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehavior."""
        super().__init__()
        self.runnable_ref: Optional[ARRef] = None
        self.td_event_swc_behavior_type: Optional[Any] = None
        self.variable_access_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventSwcInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSwcInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize runnable_ref
        if self.runnable_ref is not None:
            serialized = ARObject._serialize_item(self.runnable_ref, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNNABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_swc_behavior_type
        if self.td_event_swc_behavior_type is not None:
            serialized = ARObject._serialize_item(self.td_event_swc_behavior_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-SWC-BEHAVIOR-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_access_ref
        if self.variable_access_ref is not None:
            serialized = ARObject._serialize_item(self.variable_access_ref, "VariableAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-ACCESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehavior":
        """Deserialize XML element to TDEventSwcInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSwcInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSwcInternalBehavior, cls).deserialize(element)

        # Parse runnable_ref
        child = ARObject._find_child_element(element, "RUNNABLE-REF")
        if child is not None:
            runnable_ref_value = ARRef.deserialize(child)
            obj.runnable_ref = runnable_ref_value

        # Parse td_event_swc_behavior_type
        child = ARObject._find_child_element(element, "TD-EVENT-SWC-BEHAVIOR-TYPE")
        if child is not None:
            td_event_swc_behavior_type_value = child.text
            obj.td_event_swc_behavior_type = td_event_swc_behavior_type_value

        # Parse variable_access_ref
        child = ARObject._find_child_element(element, "VARIABLE-ACCESS-REF")
        if child is not None:
            variable_access_ref_value = ARRef.deserialize(child)
            obj.variable_access_ref = variable_access_ref_value

        return obj



class TDEventSwcInternalBehaviorBuilder:
    """Builder for TDEventSwcInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehavior = TDEventSwcInternalBehavior()

    def build(self) -> TDEventSwcInternalBehavior:
        """Build and return TDEventSwcInternalBehavior object.

        Returns:
            TDEventSwcInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
