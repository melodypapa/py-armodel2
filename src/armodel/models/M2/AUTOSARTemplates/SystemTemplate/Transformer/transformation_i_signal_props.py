"""TransformationISignalProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class TransformationISignalProps(ARObject):
    """AUTOSAR TransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cs_error_reaction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CSTransformerErrorReactionEnum,
        ),  # csErrorReaction
        "data_prototypes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataPrototype,
        ),  # dataPrototypes
        "transformer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Transformation),
        ),  # transformer
    }

    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototypes: list[DataPrototype] = []
        self.transformer: Optional[Any] = None


class TransformationISignalPropsBuilder:
    """Builder for TransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationISignalProps = TransformationISignalProps()

    def build(self) -> TransformationISignalProps:
        """Build and return TransformationISignalProps object.

        Returns:
            TransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
