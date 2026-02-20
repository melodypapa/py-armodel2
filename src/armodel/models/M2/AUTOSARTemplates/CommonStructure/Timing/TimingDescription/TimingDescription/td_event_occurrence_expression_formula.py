"""TDEventOccurrenceExpressionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpressionFormula(ARObject):
    """AUTOSAR TDEventOccurrenceExpressionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument_ref: Optional[ARRef]
    event_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    variable_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpressionFormula."""
        super().__init__()
        self.argument_ref: Optional[ARRef] = None
        self.event_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.variable_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventOccurrenceExpressionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize argument_ref
        if self.argument_ref is not None:
            serialized = ARObject._serialize_item(self.argument_ref, "AutosarOperationArgumentInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = ARObject._serialize_item(self.event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = ARObject._serialize_item(self.mode_ref, "TimingModeInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_ref
        if self.variable_ref is not None:
            serialized = ARObject._serialize_item(self.variable_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpressionFormula":
        """Deserialize XML element to TDEventOccurrenceExpressionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOccurrenceExpressionFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse argument_ref
        child = ARObject._find_child_element(element, "ARGUMENT-REF")
        if child is not None:
            argument_ref_value = ARRef.deserialize(child)
            obj.argument_ref = argument_ref_value

        # Parse event_ref
        child = ARObject._find_child_element(element, "EVENT-REF")
        if child is not None:
            event_ref_value = ARRef.deserialize(child)
            obj.event_ref = event_ref_value

        # Parse mode_ref
        child = ARObject._find_child_element(element, "MODE-REF")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse variable_ref
        child = ARObject._find_child_element(element, "VARIABLE-REF")
        if child is not None:
            variable_ref_value = ARRef.deserialize(child)
            obj.variable_ref = variable_ref_value

        return obj



class TDEventOccurrenceExpressionFormulaBuilder:
    """Builder for TDEventOccurrenceExpressionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpressionFormula = TDEventOccurrenceExpressionFormula()

    def build(self) -> TDEventOccurrenceExpressionFormula:
        """Build and return TDEventOccurrenceExpressionFormula object.

        Returns:
            TDEventOccurrenceExpressionFormula instance
        """
        # TODO: Add validation
        return self._obj
