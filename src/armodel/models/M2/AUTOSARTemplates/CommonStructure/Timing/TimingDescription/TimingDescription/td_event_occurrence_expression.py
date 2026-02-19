"""TDEventOccurrenceExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpression(ARObject):
    """AUTOSAR TDEventOccurrenceExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[AutosarOperationArgumentInstance]
    formula: Optional[Any]
    modes: list[TimingModeInstance]
    variables: list[Any]
    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpression."""
        super().__init__()
        self.arguments: list[AutosarOperationArgumentInstance] = []
        self.formula: Optional[Any] = None
        self.modes: list[TimingModeInstance] = []
        self.variables: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize TDEventOccurrenceExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = ARObject._serialize_item(item, "AutosarOperationArgumentInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize formula
        if self.formula is not None:
            serialized = ARObject._serialize_item(self.formula, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize modes (list to container "MODES")
        if self.modes:
            wrapper = ET.Element("MODES")
            for item in self.modes:
                serialized = ARObject._serialize_item(item, "TimingModeInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variables (list to container "VARIABLES")
        if self.variables:
            wrapper = ET.Element("VARIABLES")
            for item in self.variables:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpression":
        """Deserialize XML element to TDEventOccurrenceExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOccurrenceExpression object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arguments (list from container "ARGUMENTS")
        obj.arguments = []
        container = ARObject._find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.arguments.append(child_value)

        # Parse formula
        child = ARObject._find_child_element(element, "FORMULA")
        if child is not None:
            formula_value = child.text
            obj.formula = formula_value

        # Parse modes (list from container "MODES")
        obj.modes = []
        container = ARObject._find_child_element(element, "MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modes.append(child_value)

        # Parse variables (list from container "VARIABLES")
        obj.variables = []
        container = ARObject._find_child_element(element, "VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variables.append(child_value)

        return obj



class TDEventOccurrenceExpressionBuilder:
    """Builder for TDEventOccurrenceExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpression = TDEventOccurrenceExpression()

    def build(self) -> TDEventOccurrenceExpression:
        """Build and return TDEventOccurrenceExpression object.

        Returns:
            TDEventOccurrenceExpression instance
        """
        # TODO: Add validation
        return self._obj
