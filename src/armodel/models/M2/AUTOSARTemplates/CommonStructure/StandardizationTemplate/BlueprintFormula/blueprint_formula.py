"""BlueprintFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class BlueprintFormula(ARObject):
    """AUTOSAR BlueprintFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc", None, False, False, EcucDefinitionElement),  # ecuc
        ("verbatim", None, False, False, MultiLanguageVerbatim),  # verbatim
    ]

    def __init__(self) -> None:
        """Initialize BlueprintFormula."""
        super().__init__()
        self.ecuc: EcucDefinitionElement = None
        self.verbatim: MultiLanguageVerbatim = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BlueprintFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintFormula":
        """Create BlueprintFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BlueprintFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BlueprintFormula since parent returns ARObject
        return cast("BlueprintFormula", obj)


class BlueprintFormulaBuilder:
    """Builder for BlueprintFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintFormula = BlueprintFormula()

    def build(self) -> BlueprintFormula:
        """Build and return BlueprintFormula object.

        Returns:
            BlueprintFormula instance
        """
        # TODO: Add validation
        return self._obj
