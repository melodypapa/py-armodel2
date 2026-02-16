"""EcucDefinitionElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
    EcucValidationCondition,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)


class EcucDefinitionElement(Identifiable):
    """AUTOSAR EcucDefinitionElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_cond", None, False, False, any (EcucCondition)),  # ecucCond
        ("ecuc_validations", None, False, True, EcucValidationCondition),  # ecucValidations
        ("lower_multiplicity", None, True, False, None),  # lowerMultiplicity
        ("related_trace", None, False, False, Traceable),  # relatedTrace
        ("scope", None, False, False, EcucScopeEnum),  # scope
        ("upper_multiplicity", None, True, False, None),  # upperMultiplicity
    ]

    def __init__(self) -> None:
        """Initialize EcucDefinitionElement."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.ecuc_validations: list[EcucValidationCondition] = []
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.related_trace: Optional[Traceable] = None
        self.scope: Optional[EcucScopeEnum] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucDefinitionElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionElement":
        """Create EcucDefinitionElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucDefinitionElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucDefinitionElement since parent returns ARObject
        return cast("EcucDefinitionElement", obj)


class EcucDefinitionElementBuilder:
    """Builder for EcucDefinitionElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDefinitionElement = EcucDefinitionElement()

    def build(self) -> EcucDefinitionElement:
        """Build and return EcucDefinitionElement object.

        Returns:
            EcucDefinitionElement instance
        """
        # TODO: Add validation
        return self._obj
