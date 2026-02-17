"""TransformationTechnology AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 764)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.buffer_properties import (
    BufferProperties,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)


class TransformationTechnology(Identifiable):
    """AUTOSAR TransformationTechnology."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "buffer_properties": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BufferProperties,
        ),  # bufferProperties
        "has_internal": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # hasInternal
        "needs_original": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # needsOriginal
        "protocol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # protocol
        "transformation_description": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TransformationDescription,
        ),  # transformationDescription
        "transformer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TransformerClassEnum,
        ),  # transformer
        "version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # version
    }

    def __init__(self) -> None:
        """Initialize TransformationTechnology."""
        super().__init__()
        self.buffer_properties: Optional[BufferProperties] = None
        self.has_internal: Optional[Boolean] = None
        self.needs_original: Optional[Boolean] = None
        self.protocol: Optional[String] = None
        self.transformation_description: Optional[TransformationDescription] = None
        self.transformer: Optional[TransformerClassEnum] = None
        self.version: Optional[String] = None


class TransformationTechnologyBuilder:
    """Builder for TransformationTechnology."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationTechnology = TransformationTechnology()

    def build(self) -> TransformationTechnology:
        """Build and return TransformationTechnology object.

        Returns:
            TransformationTechnology instance
        """
        # TODO: Add validation
        return self._obj
