"""FormulaExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 223)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 448)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_FormulaLanguage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from abc import ABC, abstractmethod


class FormulaExpression(ARObject, ABC):
    """AUTOSAR FormulaExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_reference_refs: list[ARRef]
    atp_string_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FormulaExpression."""
        super().__init__()
        self.atp_reference_refs: list[ARRef] = []
        self.atp_string_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize FormulaExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize atp_reference_refs (list to container "ATP-REFERENCES")
        if self.atp_reference_refs:
            wrapper = ET.Element("ATP-REFERENCES")
            for item in self.atp_reference_refs:
                serialized = ARObject._serialize_item(item, "Referrable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize atp_string_refs (list to container "ATP-STRINGS")
        if self.atp_string_refs:
            wrapper = ET.Element("ATP-STRINGS")
            for item in self.atp_string_refs:
                serialized = ARObject._serialize_item(item, "Referrable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FormulaExpression":
        """Deserialize XML element to FormulaExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FormulaExpression object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse atp_reference_refs (list from container "ATP-REFERENCES")
        obj.atp_reference_refs = []
        container = ARObject._find_child_element(element, "ATP-REFERENCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.atp_reference_refs.append(child_value)

        # Parse atp_string_refs (list from container "ATP-STRINGS")
        obj.atp_string_refs = []
        container = ARObject._find_child_element(element, "ATP-STRINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.atp_string_refs.append(child_value)

        return obj



class FormulaExpressionBuilder:
    """Builder for FormulaExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FormulaExpression = FormulaExpression()

    def build(self) -> FormulaExpression:
        """Build and return FormulaExpression object.

        Returns:
            FormulaExpression instance
        """
        # TODO: Add validation
        return self._obj
