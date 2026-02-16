"""ClassContentConditional AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
    SdgTailoring,
)


class ClassContentConditional(Identifiable):
    """AUTOSAR ClassContentConditional."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AttributeTailoring,
        ),  # attributes
        "condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractCondition,
        ),  # condition
        "constraints": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConstraintTailoring,
        ),  # constraints
        "sdg_tailorings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SdgTailoring,
        ),  # sdgTailorings
    }

    def __init__(self) -> None:
        """Initialize ClassContentConditional."""
        super().__init__()
        self.attributes: list[AttributeTailoring] = []
        self.condition: Optional[AbstractCondition] = None
        self.constraints: list[ConstraintTailoring] = []
        self.sdg_tailorings: list[SdgTailoring] = []


class ClassContentConditionalBuilder:
    """Builder for ClassContentConditional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassContentConditional = ClassContentConditional()

    def build(self) -> ClassContentConditional:
        """Build and return ClassContentConditional object.

        Returns:
            ClassContentConditional instance
        """
        # TODO: Add validation
        return self._obj
