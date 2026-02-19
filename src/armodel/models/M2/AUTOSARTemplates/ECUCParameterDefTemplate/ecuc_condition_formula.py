"""EcucConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
        EcucQuery,
    )



class EcucConditionFormula(ARObject):
    """AUTOSAR EcucConditionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_query: Optional[EcucQuery]
    def __init__(self) -> None:
        """Initialize EcucConditionFormula."""
        super().__init__()
        self.ecuc_query: Optional[EcucQuery] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucConditionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize ecuc_query
        if self.ecuc_query is not None:
            serialized = ARObject._serialize_item(self.ecuc_query, "EcucQuery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-QUERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucConditionFormula":
        """Deserialize XML element to EcucConditionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucConditionFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc_query
        child = ARObject._find_child_element(element, "ECUC-QUERY")
        if child is not None:
            ecuc_query_value = ARObject._deserialize_by_tag(child, "EcucQuery")
            obj.ecuc_query = ecuc_query_value

        return obj



class EcucConditionFormulaBuilder:
    """Builder for EcucConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucConditionFormula = EcucConditionFormula()

    def build(self) -> EcucConditionFormula:
        """Build and return EcucConditionFormula object.

        Returns:
            EcucConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
