"""EcucContainerDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)


class EcucContainerDef(EcucDefinitionElement):
    """AUTOSAR EcucContainerDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_uris": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucDestinationUriDef,
        ),  # destinationUris
        "multiplicities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucMultiplicityConfigurationClass,
        ),  # multiplicities
        "origin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # origin
        "post_build_variant": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # postBuildVariant
        "requires_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # requiresIndex
    }

    def __init__(self) -> None:
        """Initialize EcucContainerDef."""
        super().__init__()
        self.destination_uris: list[EcucDestinationUriDef] = []
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None


class EcucContainerDefBuilder:
    """Builder for EcucContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerDef = EcucContainerDef()

    def build(self) -> EcucContainerDef:
        """Build and return EcucContainerDef object.

        Returns:
            EcucContainerDef instance
        """
        # TODO: Add validation
        return self._obj
