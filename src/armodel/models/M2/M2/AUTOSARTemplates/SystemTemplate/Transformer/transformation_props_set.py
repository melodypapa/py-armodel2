"""TransformationPropsSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class TransformationPropsSet(ARElement):
    """AUTOSAR TransformationPropsSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "transformation_props_propses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TransformationProps,
        ),  # transformationPropsPropses
    }

    def __init__(self) -> None:
        """Initialize TransformationPropsSet."""
        super().__init__()
        self.transformation_props_propses: list[TransformationProps] = []


class TransformationPropsSetBuilder:
    """Builder for TransformationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationPropsSet = TransformationPropsSet()

    def build(self) -> TransformationPropsSet:
        """Build and return TransformationPropsSet object.

        Returns:
            TransformationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
