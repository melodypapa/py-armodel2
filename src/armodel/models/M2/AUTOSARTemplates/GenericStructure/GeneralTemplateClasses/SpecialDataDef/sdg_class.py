"""SdgClass AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SdgAttribute,
        ),  # attributes
        "caption": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # caption
        "extends_meta": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # extendsMeta
        "sdg_constraints": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TraceableText,
        ),  # sdgConstraints
    }

    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraints: list[TraceableText] = []


class SdgClassBuilder:
    """Builder for SdgClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgClass = SdgClass()

    def build(self) -> SdgClass:
        """Build and return SdgClass object.

        Returns:
            SdgClass instance
        """
        # TODO: Add validation
        return self._obj
